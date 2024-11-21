variable "data" {
  description = "List of resources to be configured"
  type = list(object({
    name = string
    aps = list(object({
      name = string
      epgs = list(object({
        name = string
      }))
    }))
  }))
}