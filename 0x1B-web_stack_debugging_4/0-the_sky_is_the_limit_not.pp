# Puppet manifest to correct 'too many files open'

}
exec { 'ulimit':
  command  => 'sed -i "s/n 15/n 1500/" /etc//default/nginx',
  provider => 'shell',
  path     => '/usr/bin:/usr/sbin:/bin:/usr/local/sbin:/usr/local/bin:/bin:/sbin',
  before   => Exec['nginx-restart'],
}
exec { 'nginx-restart':
  command  => 'service nginx restart',
  provider => 'shell',
  path     => '/usr/bin/',  # sbin/nginx',
  require  => Exec['ulimit'],
}
# exec { 'nginx-start':
#   command     => 'nginx',
#   provider    => 'shell',
#   path        => '/usr/sbin',  # sbin/nginx',
#   require     => Exec["nginx-stop"],
# }

# file_line { 'holberton_identity':
#   ensure   => absent,
#   path     => '/etc/nginx/nginx.conf',
#   line     => 'worker_rlimit_nofile 3072;',
#   match    => ' ',
# }
