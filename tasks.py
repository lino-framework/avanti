from lino.invlib.ns import ns
ns.setup_from_tasks(
    globals(), "lino_avanti",
    languages="en de fr".split(),
    tolerate_sphinx_warnings=False,
    locale_dir='lino_avanti/lib/avanti/locale',
    revision_control_system='git',
    cleanable_files=['docs/api/lino_avanti.*'],
    demo_projects=['lino_avanti.projects.adg.settings.demo'])


