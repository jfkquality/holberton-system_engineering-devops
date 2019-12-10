# Puppet manifest to create /tmp/holberton file

file { '/tmp/holberton':
  ensure   => 'present',
  owner    => 'www-data',
  group    => 'www-data',
  mode     => '0744',
  content  => 'I love Puppet',
}
