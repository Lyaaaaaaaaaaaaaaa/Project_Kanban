flatpak-builder --force-clean --repo=./.repo .build io.github.lyaaaaaaaaaaaaaaa.Project_Kanban.yml
mkdir .bundle
flatpak build-bundle .repo .bundle/io.github.lyaaaaaaaaaaaaaaa.Project_Kanban.flatpak io.github.lyaaaaaaaaaaaaaaa.Project_Kanban master
