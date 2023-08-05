import click

from apkg import adistro
from apkg import compat
from apkg.log import getLogger, T
from apkg.project import Project


log = getLogger(__name__)


@click.command(name='status')
@click.option('-d', '--distro',
              help="override target distro  [default: current]")
@click.help_option('-h', '--help', help='show this help')
def cli_status(*args, **kwargs):
    """
    show status of current project
    """
    status(*args, **kwargs)


def status(distro=None):
    """
    show status of current project
    """
    proj = Project(auto_compat=False)

    msg = "project name:            {t.bold}{name}{t.normal}"
    print(msg.format(name=proj.name, t=T))
    msg = "project base path:       {t.bold}{path}{t.normal}"
    print(msg.format(path=proj.path.resolve(), t=T))

    msg = "project VCS:             {t.bold}{vcs}{t.normal}"
    print(msg.format(vcs=proj.vcs or 'none', t=T))

    msg = "project config:          {t.bold}{path}{t.normal}"
    if proj.config_path.exists():
        msg += " ({t.green}exists{t.normal})"
    else:
        msg += " ({t.warn}doesn't exist{t.normal})"
    print(msg.format(path=proj.config_path, t=T))

    msg = "project compat level:    {t.bold}{level}{t.normal}"
    level = proj.compat_level
    compat_ok, compat_state = compat.level_status(level)
    if level is None:
        level = 'N/A'
    if compat_ok:
        msg += " ({t.green}{state}{t.normal})"
    else:
        msg += (" ({t.warn}{state}"
                " -> run {t.command}apkg compat{t.normal})")
    print(msg.format(level=level, state=compat_state, t=T))

    msg = "package templates path:  {t.bold}{path}{t.normal}"
    if proj.templates_path.exists():
        msg += " ({t.green}exists{t.normal})"
    else:
        msg += " ({t.red}doesn't exist{t.normal})"
    print(msg.format(path=proj.templates_path, t=T))

    print("package templates:")
    if proj.templates:
        msg_lines = []
        for template in proj.templates:
            short_path = template.path.relative_to(proj.templates_path)
            msg_lines.append(
                "    {t.bold}%s{t.normal}: {t.green}%s{t.normal} %s: %s"
                % (short_path, template.pkgstyle.name,
                   template.selection_str(), template.distro_rules))
        msg = "\n".join(msg_lines)
    else:
        msg = "    {t.red}no package templates found{t.normal}"
    print(msg.format(dir=proj.templates_path, t=T))

    print()
    if distro:
        # target distro status
        distro = adistro.Distro(distro)
        msg = "target distro: {t.cyan}{id}{t.normal}"
        print(msg.format(id=distro, t=T))
    else:
        # current distro status
        distro = adistro.current_distro()
        fullname = adistro.current_fullname()
        msg = ("current distro: "
               "{t.cyan}{id}{t.normal} / {t.cyan}{full}{t.normal}")
        print(msg.format(full=fullname, id=distro, t=T))

    template = proj.get_template_for_distro_(distro)
    msg = "    package style: "
    if template:
        style = template.pkgstyle.name
        msg += "{t.green}%s{t.normal}" % style
    else:
        msg += "{t.warn}unsupported{t.normal}"
    print(msg.format(t=T))
    msg = "    package template: "
    if template:
        msg += "{t.green}%s{t.normal}" % template.path
    else:
        msg += "{t.warn}unsupported{t.normal}"
    print(msg.format(t=T))


APKG_CLI_COMMANDS = [cli_status]
