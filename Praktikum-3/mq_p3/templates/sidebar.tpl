<!-- Template -->
<!-- Navigationsbereich -->
<ul>
@var entry_a;@
@var loop_i;@
@for loop_i = 0; loop_i < context.length; loop_i++@
   @entry_a = context[loop_i];@
   <li><a href="##" data-action="#entry_a[0]#">#entry_a[1]#</a></li>
@endfor@
</ul>
<!-- EOF -->
