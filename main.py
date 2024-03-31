<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HELLO</title>
</head>
<body.style>
<button class="click_me" id="id_1">кнопка</button>
<script>
document.addEventListener("click", function(e)
{
  if_id = e . target. id;
  the_class = e . target.className;
  if(the_class == "click_me")
  {
    if_id = document.getElementById(if_id);
    if(if_id .style . background == "red")
    {
      if_id .style . background = "#efefef";
    }
    else
    {
      var links = document.querySelectorAll(".click_me");
      links.forEach(link => {
        link.setAttribute("style", "background:#efefef");
      })
      if_id .style . background = "red";
    }
  }
});
</script>
