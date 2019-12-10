# Puppet manifest to execute a command
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  path     => '/usr/bin/',
}
