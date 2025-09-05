docker run --rm -p 4000:4000 \
  -v "$PWD":/srv/jekyll \
  -e JEKYLL_ENV=development \
  jekyll/jekyll:4 \
  jekyll serve --watch --livereload
