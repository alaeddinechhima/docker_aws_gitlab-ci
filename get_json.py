import sys
import json

data ={
    "family": "flask-app",
    "containerDefinitions": [
        {
            "image": "008363129475.dkr.ecr.us-east-2.amazonaws.com/flask-app:"+str(sys.argv[1]),
            "name": "flask-app",
            "cpu": 1024,
            "memory": 300,
            "essential": True,
            "portMappings": [
                {
                    "containerPort": 5000,
                    "hostPort": 5000
                }
		]
        }
	]
}

with open('flask-app-task.json','wb') as out :
 	json.dump(data,out,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)

