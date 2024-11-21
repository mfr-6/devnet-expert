Provisioner is used to execute stripts locally or remotely.

Supported Provisioners:
1. local-exec - execute command locally
2. remote-exec - execute stricpt on a remote resource
3. file - copy files to a remote resource


Ref:
Terraform Up and Running, p. 306

When using null_resource it's possible to save command output to 'output'

```resource "null_resource" "contents" {
  triggers = {
    stdout     = "${data.external.read.result["stdout"]}"
    stderr     = "${data.external.read.result["stderr"]}"
    exitstatus = "${data.external.read.result["exitstatus"]}"
  }

  lifecycle {
    ignore_changes = [
      "triggers",
    ]
  }
} 

output "stdout" {
  value = "${chomp(null_resource.contents.triggers["stdout"])}"
}
```