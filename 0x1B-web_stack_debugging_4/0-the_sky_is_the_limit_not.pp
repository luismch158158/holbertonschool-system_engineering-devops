#This manifiest increment limit of requests per second
exec {'This manifiest modify ULIMIT':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',
  user     => 'root',
  provider => 'shell',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
