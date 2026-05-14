package kubernetes.security

deny[msg] {
  input.spec.containers[_].securityContext.privileged == true
  msg := "Privileged containers are forbidden"
}