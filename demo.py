import os
import mlflow
import argparse
import time


def evaluate(p1,p2):
    power_value=p1**2 + p2**2
    return power_value

def main(param1,param2):
    with mlflow.start_run():
        mlflow.log_param("param1",param1)
        mlflow.log_param("param2",param2)

        metric=evaluate(param1,param2)

        mlflow.log_metric("metrics", metric)

        os.makedirs("temp", exist_ok=True)

        with open("temp/loggin.txt", "w") as f:
            f.write(time.asctime())

        mlflow.log_artifact("temp")
        
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--param1","-p1",type=int,default=2)
    args.add_argument("--param2","-p2",type=int,default=5)
    parsed_args=args.parse_args()

    main(parsed_args.param1,parsed_args.param2)