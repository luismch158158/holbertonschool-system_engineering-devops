#!/usr/bin/pup
#Using Puppet, create a manifest that kills a process named killmenow.
exec {'pkill':
  command   => 'pkill killmenow',
  user      => 'root',
  provider  => 'shell',
  path      => '/usr/local/bin/:/bin:/usr/sbin',
}
