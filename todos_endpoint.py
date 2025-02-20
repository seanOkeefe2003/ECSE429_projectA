import requests
from datetime import datetime

BASE_URL = "http://localhost:4567"
LOG_FILE = "./explore_output/explore_todos.txt"

def start_new_log():
    with open(LOG_FILE, "w") as f:
        f.write("Start of tests: ")

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{message}\n")
    print(message)

def test_get_todos():
    log("\nTesting GET /todos")
    response = requests.get(f"{BASE_URL}/todos")
    log(f"Status: {response.status_code}")
    log(f"Response: {response.text}")

def test_head_todos():
    log("\nTesting HEAD /todos")
    response = requests.head(f"{BASE_URL}/todos/7")
    log(f"Status: {response.status_code}")
    log(f"Headers: {dict(response.headers)}")


    response = requests.head(f"{BASE_URL}/todos")
    log(f"\nHead without id Status: {response.status_code}")
    log(f"Headers: {dict(response.headers)}")


def test_post_todos():
    log("\nTesting POST /todos")
    
    # Test creating a todo
    todo = {
        "title": "Test todo",
        "description": "Test description",
        "doneStatus": False
    }
    response = requests.post(f"{BASE_URL}/todos", json=todo)
    log(f"POST new todo - Status: {response.status_code}")
    log(f"Response: {response.text}")
    
    # Test missing title
    bad_todo = {
        "description": "No title here"
    }
    response = requests.post(f"{BASE_URL}/todos", json=bad_todo)
    log(f"\nPOST without title - Status: {response.status_code}")
    log(f"Response: {response.text}")

    #Test creating a todo with done status as a string
    done_as_string_todo = {
        "title": "Test todo",
        "description": "Test description",
        "doneStatus": "False"
    }
    response = requests.post(f"{BASE_URL}/todos", json=done_as_string_todo)
    log(f"\nPOST new todo with done status as string - Status: {response.status_code}")
    log(f"Response: {response.text}")

def run_tests():
    start_new_log() 
    test_get_todos()
    test_head_todos()
    test_post_todos()
    log("\nTests completed")
    log(f"Results saved to {LOG_FILE}")

if __name__ == "__main__":
    run_tests()