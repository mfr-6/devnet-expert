variable "bridge_domains" {
  description = "List of BD objects"
  type = list(object({
    name               = string
    description        = string
    l2_unknown_unicast = string
  }))
  validation {
    condition     = alltrue([for value in var.bridge_domains : contains(["", "proxy", "flood"], value.l2_unknown_unicast)])
    error_message = "Allowed values for: l2_unknown_unicast attribute: '', 'proxy' or 'flood'. Default: 'proxy'."
  }
  default = [
    {
      name               = "mfr-bd1"
      description        = "this is bd1"
      l2_unknown_unicast = ""
    },
    {
      name               = "mfr-bd2"
      description        = "this is bd2"
      l2_unknown_unicast = "flood"
    },
    {
      name               = "mfr-bd3"
      description        = "this is bd3"
      l2_unknown_unicast = "flood"
    },
    {
      name               = "mfr-bd4"
      description        = "this is bd4"
      l2_unknown_unicast = "proxy"
    }
  ]
}