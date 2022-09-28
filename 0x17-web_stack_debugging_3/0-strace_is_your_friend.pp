#!/usr/bin/puppet
# In order to see the php errors, what we do is activate PHP logging in php.ini
# In this path you will find the php configuration /etc/php5/apache2/php.ini
# we change the following instructions display_errors = On, display_startup_errors = On, error_reporting = E_ALL
# Then we restart PHP and Apache for the change to take effect
# Then when doing the CURL it already shows us the error:
# <b>Fatal error</b>:  require_once(): Failed opening required '/var/www/html/wp-includes/class-wp-locale.phpp'
# In which we can see that it is looking for a file that has a .phpp extension
#and not php as it should be, so we look for it in the configuration file and change it
# For that we enter the wordpress configuration file in the following path /var/www/html/wp-settings.php,
#and we make the change with the sed command from phpp to php and the error is solved


exec {'change phpp in configuration':
  command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  user     => 'root',
  provider => 'shell',
  path     => '/usr/local/bin/:/bin:/usr/sbin'
}
