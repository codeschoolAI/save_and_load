import requests
import numpy as np

class CheckSolution:
    def __init__(self, task_name):
        self.task_name = task_name
        self.url = "https://codeschoolhomeworkapi.pythonanywhere.com/homework/attempt/"
    def checking(self, github_username, isSolved, homework_name):

        """
        Chack if the solution is correct

        Args:
            solution (np.ndarray): solution to check
            github_username (str): github username

        Returns:
            bool: True if the solution is correct
        """

        data = {
            'github': github_username,
            'repo': f'AIGroup/{homework_name}',
            'tasks': [
                {'isSolved': bool(isSolved), 'name': self.task_name}]
            }

        response = requests.post(self.url, json=data)

        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        print(response.status_code)

class LoadNpy(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution.__class__ == np.ndarray
    
    def test_case_2(self, solution):
        try:
            return solution.shape == (350, 350, 3)
        except:
            return False
    
    def check(self,solution, github_username):
        case1 = self.test_case_1(solution)
        case2 = self.test_case_2(solution)
        isSolved = all([case1, case2])
        self.checking(github_username, isSolved, self.homework_name)

class MergeImage(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        return solution.__class__ == np.ndarray
    
    def test_case_2(self, solution):
        try:
            return solution.shape == (700, 700, 3)
        except:
            return False
    
    def test_case_3(self, solution):
        try:
            return bool(np.equal(solution[350,350], np.array([1,20,34])).all())
        except:
            return False
        
    def check(self,solution, github_username):
        case1 = self.test_case_1(solution)
        case2 = self.test_case_2(solution)
        case3 = self.test_case_3(solution)
        isSolved = all([case1, case2, case3])
        self.checking(github_username, isSolved, self.homework_name)

q0 = LoadNpy(task_name="load_npy", homework_name="save_and_load")
q1 = MergeImage(task_name="merge_image", homework_name="save_and_load")