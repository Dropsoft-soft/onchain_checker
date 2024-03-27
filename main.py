import requests


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_example(url):
    response = requests.get(url)
    return response.text


def post_example(url, data):
    response = requests.post(url, data=data)
    return response.text


def test_res():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = get_example(url)
    print("GET response:", response)

    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = post_example(url, data)
    print("POST response:", response)


if __name__ == '__main__':
    print_hi('D_O_C_K_E_R')
    test_res()

