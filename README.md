### VirtualBox

* [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  
* Install the *platform package* for your operating system.  
* You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.


### Vagrant

* [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.


## Fetch the Source Code and VM Configuration

* From the terminal, run:

    * git clone https://github.com/udacity/OAuth2.0 oauth

* This will give you a directory named **oauth** complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools.

## Run the virtual machine!

* Using the terminal, change directory to oauth (**cd oauth**), then type **vagrant up** to launch your virtual machine.


## Running the Catalog App
* Once it is up and running, type **vagrant ssh**.
* Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.  
* change to the /vagrant directory by typing **cd /vagrant**.
* Now type **python database_setup.py** to initialize the database.
* Type **python populate.py** to populate the database with categories and items. (Optional)
* Type **python project.py** to run the Flask web server.
* In your browser visit **http://localhost:5000** to view the restaurant menu app.  You should be able to view, add, edit, and delete menu items and restaurants.

## Helpful links
* [README.md file](https://github.com/udacity/OAuth2.0)
* [rrjoson's udacity-item-catalog](https://github.com/rrjoson/udacity-item-catalog)
* Udacity's Restaurant Menu App Project
