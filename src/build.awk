FILENAME != template {
	if (/\t/ && !/^#/) {
		val = $0; sub(/^[^\t]+\t+/, "", val)
		k = $0; sub(/\t.*/, "", k)
		v[k] = val
	}
	next
}

!resolved {
	for (k in v)
		for (j in v)
			gsub("[{]" j "[}]", v[j], v[k])
	resolved = 1
}

{
	for (k in v)
		gsub("[{]" k "[}]", v[k])
	print
}
