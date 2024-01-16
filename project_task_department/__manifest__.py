# © 2023 Serincloud ( https://www.ingenieriacloud.com )
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Project task departments",
    'summary': """
        Proyect Task departments
        """,
    'author': 'Serincloud',
    'license': 'AGPL-3',
    'website': "https://ingenieriacloud.com",
    'category': 'Project',
    'version': '16.0.1.0.0',
    'depends': [
        'project',
        'hr',
    ],
    'data': [
        'views/project_task_views.xml',
    ],
    'installable': True,
    'application': False,
}
