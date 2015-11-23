# Example paas django app

This is an example web application based on django and django-edge project, 
ready to be used to deploy your own webapp on Synnefo PaaS service.

### Quick start

- Install the deis client:

    $ curl -sSL http://deis.io/deis-cli/install.sh | sh
    $ mv deis <path-to-your-bins-dir>

- Login to the Synnefo PaaS using your API credentials
    
    $ deis login https://deis.platform.demo.synnefo.org

- Add your public ssh key to be able to push to the PaaS git remote

    $ deis keys:add
    
- Clone the example project

    $ git clone https://github.com/grnet/platform-django-example my-django-app
    $ cd my-django-app

- Create a new application using,

    $ deis create my-django-app -r paas

- Initialize your application configuration
    
    $ deis config:set SECRET_KEY="<secret-key>"
    $ deis config:set PYTHONUNBUFFERED=True
    $ deis config:set ALLOWED_HOSTS="localhost,my-django-app.platform.demo.synnefo.org"
    $ deis config:set ENVIRONMENT=production
    $ deis config:set PG=enabled

- The last setting will create and initialize a postgresql database to be used   
  from your running application.

- At last push your application code to the PaaS service

  $ git push paas

- You may now initialize your database by running

  $ deis run 


Management
==========

* Use "deis logs" to view the logs of your application
* Use "deis scale web=X" to scale up/down your application processes
