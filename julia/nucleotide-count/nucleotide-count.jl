"""
    count_nucleotides(strand)

The count of each nucleotide within `strand` as a dictionary.

Invalid strands raise a `DomainError`.

"""
function count_nucleotides(strand)
	ans = Dict('A' => 0, 'C' => 0, 'G' => 0, 'T' => 0)
	if length(strand) == 0
		return ans
	else	
		for i in 1:length(strand)
			if strand[i] == 'A'
				ans['A'] += 1
			elseif strand[i] == 'C'
	    			ans['C'] += 1
	    		elseif strand[i] == 'G'
	    			ans['G'] += 1
	    		elseif strand[i] == 'T'
	    			ans['T'] += 1
			else
	    			throw(DomainError(strand))
			end
		end
		return ans
	end
end
