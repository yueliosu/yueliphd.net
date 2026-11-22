-- mark R output blocks (code with no language) so they can be styled as output
function CodeBlock(el)
  if #el.classes == 0 then el.classes = {'r-output'} end
  return el
end
-- unwrap rmarkdown's <div class="section"> wrappers; headings carry the structure
function Div(el)
  if el.classes:includes('section') then return el.content end
end
