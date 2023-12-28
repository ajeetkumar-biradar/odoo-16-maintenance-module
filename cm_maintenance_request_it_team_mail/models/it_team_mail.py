from odoo import models, fields, api


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    @api.model
    def create(self, values):
        maintenance_request = super(MaintenanceRequest, self).create(values)

        # Send email notification to assignees
        if maintenance_request.team_members:
            maintenance_request.send_notification_email_to_team(maintenance_request.team_members)

        return maintenance_request

    def write(self, values):
        result = super(MaintenanceRequest, self).write(values)

        # Send email notification to assignees if team_members is updated
        if 'team_members' in values:
            self.send_notification_email_to_team(self.team_members)

        return result

    def send_notification_email_to_team(self, team_members):
        subject = "Maintenance Request Assigned: {}".format(self.name)

        # Get a comma-separated list of team member names
        team_member_names = ", ".join(member.name for member in team_members)

        # Include the description if it exists
        body = "Dear {},<br><br>You have been assigned to a Maintenance Request!<br><br>Request Name: {}<br>".format(
            team_member_names, self.name)

        if self.description:
            body += "Description: {}<br>".format(self.description)

        body += "<br>Thank You."

        # Send the email to the team members
        partner_ids = [member.partner_id.id for member in team_members]
        self.message_post(body=body, subject=subject, partner_ids=partner_ids,
                          subtype_id=self.env.ref('mail.mt_comment').id)
