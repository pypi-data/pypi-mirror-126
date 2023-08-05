from requests import get
from threading import Thread
from time import sleep

class Gitlab(Thread):
    def __init__(self, gitlab_url : str, group_id : str, token : str = None) -> None:
        Thread.__init__(self)
        self.__gitlab_url = gitlab_url if gitlab_url[-1] != "/" else gitlab_url[:-1]
        self.__headers = {}
        self.__continue = True

        self.__api_url = self.__gitlab_url + "/api/v4"
        self.__groups_path = "/groups"
        self.__projects_path = "/projects"
        self.__variables_path = "/variables"
        self.__group_id = group_id
        self.__projects = {}

        if token != None:
            self.__headers["PRIVATE-TOKEN"] = token
        self.__group_projects_url = self.__api_url + self.__groups_path + f"/{self.__group_id}" + self.__projects_path
    
    @property
    def variables_path(self):
        return self.__variables_path
    
    @property
    def projects_path(self):
        return self.__projects_path
    
    @property
    def api_url(self):
        return self.__api_url

    @property
    def headers(self):
        return self.__headers
    
    @property
    def projects(self):
        return self.__projects

    def get_projects(self):
        page = 1
        while self.__continue and len(response := get(self.__group_projects_url, headers = self.__headers, params = {"simple" : False, "include_subgroups" : True, "page": page, "per_page": 100, "order_by": "name", "sort": "asc"}).json()) > 0:
            for project in response:
                if not project["id"] in self.__projects and not project["archived"] and self.__continue:
                    self.__projects[project["id"]] = Project(gitlab = self, project_id = project["id"], project_name = project["name"])
            page += 1
        return self.__projects
    
    def stop(self):
        self.__continue = False
    
    def run(self):
        while self.__continue:
            self.get_projects()

class Project:
    def __init__(self, gitlab: Gitlab, project_id : int, project_name : str) -> None:
        self.__project_id = project_id
        self.__project_name = project_name
        self.__gitlab = gitlab
        self.__variables = {}
    
    @property
    def project_name(self):
        return self.__project_name
    
    @property
    def variables(self):
        return self.__variables
    
    def __str__(self) -> str:
        return f"Project({self.__project_name})"
    
    def __repr__(self) -> str:
        return self.__str__()

    def __get_variables(self):
        variables_url = self.__gitlab.api_url + self.__gitlab.projects_path + f"/{self.__project_id}" + self.__gitlab.variables_path
        for variable in get(variables_url, headers = self.__gitlab.headers).json():
            if not variable["key"] in self.__variables:
                self.__variables[variable["key"]] = Variable(gitlab = self.__gitlab, project = self, name = variable["key"])
            self.__variables[variable["key"]].add_env(variable["environment_scope"], variable["value"])
        return self.__variables

    def fetch_project(self):
        th = Thread(target = self.__get_variables)
        th.start()
        return th

class Variable:
    def __init__(self, gitlab : Gitlab, project : Project, name : str) -> None:
        self.__gitlab = gitlab
        self.__project = project
        self.__name = name
        self.__envs = {}
    
    def add_env(self, env : str, value : str):
        self.__envs[env] = value
    
    @property
    def envs(self):
        return self.__envs
    
    @property
    def name(self):
        return self.__name
    
    def __str__(self) -> str:
        return f"{self.__name}({[env_name for env_name in self.__envs]})"
    
    def __repr__(self) -> str:
        return self.__str__()