# set up ssh config file; ~/.ssh/holberton; no password
exec { 'identity':
  command  => 'echo IdentityFile ~/.ssh/holberton >> /etc/ssh/ssh_config',
  provider => 'shell',
  path     => '/usr/bin/',
}
exec { 'no_password':
  command  => 'echo IdentityFile ~/.ssh/holberton >> /etc/ssh/ssh_config',
  provider => 'shell',
  path     => '/usr/bin/',
}

# file_line { 'holberton_identity':
#   ensure            => absent,
#   path              => '/2-ssh_config',
#   line              => 'PasswordAuthentication yes',
#   match_for_absence => true,
# }
# file_line { 'no_password':
#   ensure            => absent,
#   path              => '/etc/ssh/ssh_config',
#   path              => '2-ssh_config',
#   line              => 'IdentityFile ~/.ssh/holberton',
#   match_for_absence => true,
# }
