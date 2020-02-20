# Puppet manifest to edit wp-settings.php
exec { 'sed':
  command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  provider => 'shell',
  path     => '/bin/',
}
