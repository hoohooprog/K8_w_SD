ok###
#
# 28 jan 2025 afternoon, i have some ideas and links
# to iterate, to mostly use AWS console
# so I can understand the basics visually what AWS has to offer
# before I switch to terraform to gain the blueprints to scale
# 
# source 1:  https://medium.com/@chinmayd49/self-host-llm-with-ec2-vllm-langchain-fastapi-llm-cache-and-huggingface-model-7a2efa2dcdab
#   - running ec2 thru console
#   - start time and end time code for latency
# source 2:  nlp cloud - deploy the Mistral 7b Gen model on an A10 GPU on AWS 
#   - aws console, mistral 7b, 
# source 2a: simpler form from nlpcloud, just pip vLLM, could ignore ray and no HF
#   - https://nlpcloud.com/deploy-llama-2-mistral-and-mixtral-on-aws-ec2-with-vllm.html,


# misc: 
# - eksctl delete cluster my-demo-cluster --region us-east-1 by mudasir - setup k8s cluster on EKS (shows how to create cluster n node)
# - self-host llama 3.1 88B in EC2 using VLLM and Docker by Mohamed Amri show good example of setup by console
# - "If you already have the model artifacts on your infrastructure you can use them directly by pointing vLLM to their local path 
#    instead of a Hugging Face model ID. 
#    In this scenario you will be able to skip all Hugging Face related setup steps."
#   https://docs.mistral.ai/deployment/self-deployment/vllm/
# - also see prod metrics and distributed inference and serving on vLLM official docs

# - https://www.reddit.com/r/MachineLearning/comments/1apxg42/d_deploy_mixtral_8x7b_llama_2_and_mistral_on_aws/
#   link above provides additional idea for compute, latency n request rate costs.

# so I need to download vLLM and mistral to cloud via SSH, if not from HF, and point to the mistral path like this LLM("/mistral/path")

##### conclusion #####
##  algo:
##  1) follow nlpcloud first
##  2) check ssh from chinmay
##  3) download mistral and vllm (nlpcloud)
##  4) point to directory and test generation
##  5) terminate EC2 isntance (or eksctl delete cluster)
##
##  so we would've learnt to configure ec, install vLLM and OS model for personal usage 
##  then we will understand better how to scale better for prod using EKS (from console->CLI/SSH?), Load Balancers and FastAPI
##  (see other tutorials like vic Gu's for arch and add. (AWS) services, articles that uses eks console eg mudasir, to aws workshop schema)

## our app will probably end up like Gu and aws workshop schema, where the entry(endpoints) would be the UIs such as login, transcript and translate page
## for the AI apps to process and return the data to the appropriate features on certain pages, such as the page with embedded utube vid with overlayed subs.
#####
# It would be similar to reinventing the internet/WWW, creating my own personal network and allowing specific communication from different categories of people
###

##############################################
###############################################
## 8 feb, 2025, Sat
##########################
#
# from 0900 - 1330
# reviewed materials accrued to be implemented and wrote in slides "Mistral on aws"
# if all goes well, we need to open an S3 or EBS monthly to store model, script
# to be loaded on ec2 instance. 
#
# need to link to web openUI if I want to access via web interface.
#
# 
###########################
### 9 Feb 2025, Sun
###############
###
# 1554
# sth felt wrong, that I have to go thru many hoops to even access IP
# to use AI, which isn't the point of cloud usage

# I should be able to enter an IP that shows open webUI to access a chat model
# and then have some sort of service that starts the server and run the apps
# when pinged

# for eg I should be able to easily spin up an instance like this eg with
# open webui n ollama, switching out ollama w/ vllm
# # #https://www.linkedin.com/pulse/step-by-step-launching-ollama-server-web-ui-amazon-ec2-emesoft
# -jsc-0oc6c

# since a local server works the same as the cloud server, here are the scripts to vllm
# http://varnitkhanna.com/notes/open-webui-local-vllm-model/

# from this CGPT chat https://chatgpt.com/c/67a8c887-3254-8013-866b-3ce0b0aefd07
# we can minimally spin up a open webUI and Mistral instruct chatbot
# and set up conditions to spin down

# should i automate termination of instance instead of just stopping? how? 
# lambda eg in cgpt?
#
# then we can connect other services like YouTube transcription and translation 
# in its own container and share data to the container of Mistral chat.
# from that instance, to support multi users, we would use k8s to orchestrate
# clusters of node instances

# other important features would include:
#		- chat questions and answers based on media previously questioned by other users
#		( requires caching, DB, multi lingual support , going into open webUI code 
#		 RAG top comments/answers, if not prompt user "sorry non top prompts or comments are
# 		 not updated, please specify the prompt and then your comments" )
#		- like and comment system
#		- categorizing and only featuring types of comments that user wants to see
#
#	1738

# with better understanding of this, I can also setup stable diffusion n experiment
# LoRA n increase capabilities of existing models.. 

# while adding of other features would enable me to get experience hosting large
# numbers of users 
# 1747
###
