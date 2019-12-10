# Puppet manifest to execute a command
exec { 'pkill':
  command => 'pkill killmenow',
  provide => 'shell',
}
