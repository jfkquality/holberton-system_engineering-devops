# set up ssh config file; ~/.ssh/holberton; no password

file_line { 'holberton_identity':
  ensure            => absent,
  path              => '/etc/ssh/ssh_config',
  line              => 'PasswordAuthentication yes',
  match_for_absence => true,
}
file_line { 'no_password':
  ensure            => absent,
  path              => '/etc/ssh/ssh_config',
  line              => 'IdentityFile ~/.ssh/holberton',
  match_for_absence => true,
}
