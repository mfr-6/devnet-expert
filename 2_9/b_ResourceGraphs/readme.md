Graph presented in this repo was generated outside of CWS. I just executed "terraform graph" and then copied output to the external machine and then I used dot -Tsvg > graph.svg.
graphViz (and dot) is not present in CWS, so I've added this to see how Resource Graph looks like as a visual representation

I also added here custom aci_rest resource with "depends_on" to add extra connection between resources to the Resource Graph