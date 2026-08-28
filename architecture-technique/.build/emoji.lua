ReplacementTable = {
  fast_forward= "fast-forward",
  arrow_up_small= "up-arrow",
  left_right_arrow= "left-right-arrow",
  point_right= "point-right"
}

function Str(content)
    local s=pandoc.utils.stringify(content)
    local start = 0
    local result = {}
    local i, j = string.find(s, ":[a-z-_]+:")
    while i do
      table.insert(result, pandoc.Str(string.sub(s, start, i-1)))
      emoji = string.sub(s, i+1, j-1)
      if ReplacementTable[emoji] then
        emoji = ReplacementTable[emoji]
      end
      table.insert(result, pandoc.RawInline('latex', string.format('\\emoji{%s}', emoji)))
      start = j+1
      i,j = string.find(s, ":[a-z-]+:", start)
    end
    table.insert(result, pandoc.Str(string.sub(s, start)))
    
    return result
end
