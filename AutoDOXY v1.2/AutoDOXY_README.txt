v1.2 CHANGELOG:
+Added error message for incorrect pipe placement
+Added autorunning of second command assuming preformatting
+Added auto removal of a temporary file
-----------------------------------------------

To properly use these 2 included scripts:

1. Create a blank file

2. Copy comments from original file into blank file such that they look approximately like this:
   Spaces do not matter, it is ok if there is no * character

  !     * DATE - NAME/NAME COMMENTCOMMENTCOMMENTCOMMENT:
  !     *                          - COMMENTCOMMENTCOMMENTCOMMENT
  !     *                            COMMENTCOMMENT
  !     * DATE - NAME COMMENTCOMMENTCOMMENTCOMMENT

3. Format the file such that it looks like this (where every comment is all on the "same line" [even if it takes multiple lines]):

  !     * DATE - NAME/NAME COMMENTCOMMENTCOMMENTCOMMENT: - COMMENTCOMMENTCOMMENTCOMMENTCOMMENTCOMMENT
  !     * DATE - NAME COMMENTCOMMENTCOMMENTCOMMENT

4. Run COMMAND
   ---------------------------------------------------------------------------------------------
   python3 del_cmnt.py X 
   Where X is the name of the file you created with just the comments (no formatting done yet)
   ---------------------------------------------------------------------------------------------

   COMMAND #2 is autorun and requires no input, if there is an error in formatting you will need
   to check your pipe placement
   ---------------------------------------------------------------------------------------------
   python3 cmnt_to_html.py X_final
   Where X_final is the name of the file you formatted
   ---------------------------------------------------------------------------------------------

5. Run doxygen and do any necessary corrections to the file to get desired result

