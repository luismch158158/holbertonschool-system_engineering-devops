#Configured ssh client use private key and refuse to authenticate a password
file_line {'change private key':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}

file_line {'change to refuse to authenticate using passowrd':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
