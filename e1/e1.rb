# Project euler 1

# v1
class E1
  def calc x
    sum = 0
    for i in (0..x)
      if i % 5 == 0 or i % 3 == 0 then
        sum += i 
      end
    end
    sum
  end
end
e = E1.new
puts e.calc 999

# v2
sum = 0
for i in (0..999)
  if i % 5 == 0 or i % 3 == 0 then
    sum += i 
  end
end
puts sum

# v3
s = (0..999).inject(0) do |sum,x| 
  if x%5 == 0 or x%3 == 0 then
    sum + x 
  else
    sum
  end
end

puts s
