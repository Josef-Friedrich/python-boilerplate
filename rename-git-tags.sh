#! /bin/sh

git fetch origin

# https://gist.github.com/knu/111055
# Rename tags named foo-bar-#.#.# to v#.#.# and push the tag changes
git tag -l | while read TAG; do
  NEW="v$TAG"
  git tag $NEW $TAG
  # git push --tags
  git tag -d $TAG
  # git push origin :refs/tags/$TAG
done

git push --tags --prune origin refs/tags/*
