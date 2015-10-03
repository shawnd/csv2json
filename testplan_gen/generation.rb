names = ["Alphanumeric", "Alphanumeric and Special", "Only Special"]
extensions = ["csv", "no", "other"]
exists = ["yes", "no"]
validity = ["valid", "invalid"]
oss = ["windows", "linux"]
i=0

for name in names
	for extension in extensions
		for exist in exists
			for valid in validity
				print "\n\nIteration: " + i.to_s + "\n"
				print "File name contains: " + name + "\n"
				print "Extension: " + extension + "\n"
				print "File Exists: " + exist + "\n"
 				print "Valid Format: " + valid + "\n"
 				i=i+1
 			end
 		end
 	end
end