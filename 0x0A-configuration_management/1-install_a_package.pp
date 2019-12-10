# Puppet manifest to add puppet-lint package
packagefile { 'puppet-lint':
  ensure => present,
}
