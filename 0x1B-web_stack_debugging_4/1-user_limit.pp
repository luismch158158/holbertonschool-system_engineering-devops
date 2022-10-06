# This manifiest change limit user Limit for open files with Holberton User
exec{'Change Limit open file':
  command  => 'sed -i "s/hard nofile 5/hard nofile 5000/" /etc/security/limits.conf;\
  sed -i "s/soft nofile 4/soft nofile 5000/" /etc/security/limits.conf',
  user     => 'root',
  provider => 'shell',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
