To properly use these 2 included scripts:

1. Create a blank file

2. Copy comments from original file into blank file such that they look approximately like this:
   Spaces do not matter, it is ok if there is no * character

  !     * DATE - NAME/NAME COMMENTCOMMENTCOMMENTCOMMENT:
  !     *                          - COMMENTCOMMENTCOMMENTCOMMENT
  !     *                            COMMENTCOMMENT
  !     * DATE - NAME COMMENTCOMMENTCOMMENTCOMMENT

3. Run COMMAND #1
   ---------------------------------------------------------------------------------------------
   python3 del_cmnt.py X 
   Where X is the name of the file you created with just the comments (no formatting done yet)
   ---------------------------------------------------------------------------------------------

4. Format the output file "X_final" such that it looks like this (where every comment is all on the "same line" [even if it takes multiple lines]):

DATE - NAME/NAME COMMENTCOMMENTCOMMENTCOMMENT: - COMMENTCOMMENTCOMMENTCOMMENTCOMMENTCOMMENT
DATE - NAME COMMENTCOMMENTCOMMENTCOMMENT

5. Run COMMAND #2
   ---------------------------------------------------------------------------------------------
   python3 cmnt_to_html.py X_final
   Where X_final is the name of the file you formatted
   ---------------------------------------------------------------------------------------------

6. Run doxygen and do any necessary corrections to the file to get desired result
