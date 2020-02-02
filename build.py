from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()

    transformed_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        if settings["compiler"] != "Visual Studio" and settings["arch"] == "x86":
        	pass
        else:
            transformed_builds.append([settings, options, env_vars, build_requires, reference])

    if transformed_builds:
        builder.builds = transformed_builds

    builder.run()
