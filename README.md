I create a simple flask app displaying a simple message "Welcome to my world"
In fact inthis tutorial we will deal only with the build of our docker and its deployement into aws

what we need is only that we already have our server running and we only need in case we did any change of the code, our docker will be builded and deployed into aws
Never forget with gitlabCI we successfuly update our service.

So you should note 4 variables to set them as environement variables in gitlab : AWS_Region , Image_URI and your AWS credentials

We begin by setting these variables then you can take a look of our .gitlab-ci.yml file where thanks to gitlab for giving us an easy way to automate the build of docker first of all, then the push of the image to aws repository and finaly to update the service

We use here a script to generate a json file in gitlab-ci where we set all task's revision and configuration 	

I hope it was benificial for you

Enjoy Continuous Integration
