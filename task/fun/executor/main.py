import requests

url = "https://jokeapi-v2.p.rapidapi.com/joke/Programming"

headers = {
    'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com",
    'x-rapidapi-key': "35e5d7a407msh516e031e52f9e92p16f7c3jsn196523c88ae2"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


optimus_host = os.environ["OPTIMUS_HOSTNAME"]
scheduled_at = os.environ["SCHEDULED_AT"]
project_name = os.environ["PROJECT"]
job_name = os.environ["JOB_NAME"]

print(optimus_host)
print(scheduled_at)
print(project_name)
print(job_name)