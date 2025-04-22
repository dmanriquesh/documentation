===============
Property fields
===============

Property fields, or properties, enable the customization of a :ref:`form
<studio/views/general/form>` view by adding various :ref:`field types <property_field/add>`. These
fields allow information storage and management by adding values.

.. admonition:: Property vs. regular fields

   Properties act as pseudo-fields; they behave like regular fields but are not saved as columns in
   the database. They also rely on a parent-child relationship, appearing only when a specific
   record is selected.

   .. example::
      Adding a property to a *task* includes a property field in *all tasks* within the *same
      project*, while other projects' tasks remain unaffected.

.. _property_field/add:

Add property fields
-------------------

To add a first property field to a :ref:`form view <studio/views/general/form>`, click the
:icon:`fa-cog` (:guilabel:`Actions`) icon, then select :icon:`fa-cogs` :guilabel:`Add Properties`.

In the popover, enter the property's :guilabel:`Label`, choose a :guilabel:`Field Type` among the
selection below, and then configure the field based on the selected type:

.. list-table::
   :header-rows: 1
   :widths: 15 30 55

   * - Field type
     - Use
     - Options
   * - :ref:`Text <studio/fields/simple-fields-text>`
     - Short text on a single line
     - Enter a :guilabel:`Default Value` if desired.
   * - :ref:`Checkbox <studio/fields/simple-fields-checkbox>`
     - Checked or unchecked status
     - Choose the :guilabel:`Default State`.
   * - :ref:`Integer <studio/fields/simple-fields-integer>`
     - Integer numbers (:dfn:`positive, negative, or zero, without a decimal`)
     - Enter a :guilabel:`Default Value` if desired.
   * - :ref:`Decimal <studio/fields/simple-fields-decimal>`
     - Decimal numbers (:dfn:`positive, negative, or zero, with a decimal`)
     - Enter a :guilabel:`Default Value` if desired.
   * - :ref:`Date <studio/fields/simple-fields-date>`
     - Selection of a date on a calendar
     - Select a :guilabel:`Default Value` if desired.
   * - :ref:`Date & Time <studio/fields/simple-fields-date-time>`
     - Selection of a date on a calendar and a time on a clock
     - Select a :guilabel:`Default Value` if desired.
   * - :ref:`Selection <studio/fields/simple-fields-selection>`
     - Selection of a value from a group of predefined values
     - Add a selectable option by clicking :icon:`fa-plus` :guilabel:`Add a Value` and entering the
       :guilabel:`Option Name`.

       If desired, set an option as default by clicking the :icon:`fa-star-o`
       (:guilabel:`Select Default`) button.

       Reorder the options by dragging and dropping them using the :icon:`oi-draggable`
       (:guilabel:`drag handle`) button.

       Delete an option by clicking the :icon:`fa-trash-o` (:guilabel:`Remove Property`) button.
   * - :ref:`Tags <studio/fields/relational-fields-tags>`
     - Selection of multiple values in the form of tags
     - Enter a :guilabel:`Tag` name and press `Enter` to save it.

       Change a tag's color by clicking it and selecting another one.
   * - :ref:`Many2one <studio/fields/relational-fields-many2one>`
     - Selection of a single record from another model
     - Enter the :guilabel:`Model` name. Configure its :ref:`Domain <search/custom-filters>` to
       filter records if needed.

       Select a :guilabel:`Default Value` if desired.
   * - :ref:`Many2many <studio/fields/relational-fields-many2many>`
     - Selection of multiple records from another model
     - Enter the :guilabel:`Model` name. Configure its :ref:`Domain <search/custom-filters>` to
       filter records if needed.

       Select a :guilabel:`Default Value` if desired.
   * - :guilabel:`Separator`
     - Group several properties under a foldable label
     -

Click outside the popover to save the added property.

.. note::
   - Select whether to display the property in the Kanban or Calendar views cards for every field
     with the :guilabel:`Display in Cards` option.
   - To add another property, click :icon:`fa-plus` :guilabel:`Add a Property` at the bottom of the
     form while in :icon:`fa-cogs` :guilabel:`Add Properties` mode.

.. tip::
   To edit an existing property, hover the cursor over the property:

   - Click the :icon:`fa-pencil` (:guilabel:`pencil`) button to open a popover and modify the
     property. In the popover, click the :icon:`fa-chevron-up` (up) or :icon:`fa-chevron-down`
     (down) chevron to move a property upwards or downwards.
   - Click :icon:`fa-trash` :guilabel:`Delete`, then :guilabel:`Delete` to delete it. Deleting
     a property is permanent.
   - Use the :icon:`oi-draggable` (:guilabel:`drag handle`) icon to drag and drop the property to
     reorder or regroup.

Properties across modules
-------------------------

Property fields apply to several apps in various contexts, as they are dependent on a parent record.

  .. list-table::
        :widths: 20 35 45
        :header-rows: 1
        :stub-columns: 1

        * - App
          - Action
          - Context
        * - :guilabel:`Accounting`
          - Registering :ref:`assets <create-assets-entry>`.

            Tracking :doc:`loans </applications/finance/accounting/bank/loans>`.
          - Depending on the **asset model**.

            Depending on the **journal**.
        * - :guilabel:`Appraisal`
          - Conducting an :ref:`employee appraisal <appraisals/configuration>`.
          - Depending on the **department**.
        * - :guilabel:`Approvals`
          - Submitting approval requests.
          - Depending on **requests per record**.
        * - :guilabel:`CRM`
          - Managing a :doc:`lead record </applications/sales/crm/acquire_leads/email_manual>`.
          - Depending on the **sales team**.
        * - :guilabel:`Employee`
          - Configuring an :ref:`employee record <employees/general-info>`.
          - Depending on the **company**.
        * - :guilabel:`Events`
          - Checking :doc:`event registrations </applications/marketing/events/registration_desk>`.
          - Depending on event **attendees**.
        * - :guilabel:`Fleet`
          - Registering a :doc:`vehicle </applications/hr/fleet/new_vehicle>`.
          - Depending on the **vehicle model**.
        * - :guilabel:`Frontdesk`
          - Checking a :ref:`visitor list <frontdesk/list>`.
          - Depending on **station visitors**.
        * - :guilabel:`Helpdesk`
          - Following :ref:`Helpdesk tickets <helpdesk/follow>`.
          - Depending on the Helpdesk **team**.
        * - :guilabel:`Inventory`
          - Modifying a :ref:`Lot/Serial number <inventory/product_management/edit-lot>`.

            Monitoring operation transfers.

            Creating and processing :ref:`Batch transfers <inventory/misc/batch_picking>`.
          - Depending on **product variants**.

            Depending on the **operation type**.

            Depending on the **operation type**.
        * - :guilabel:`Knowledge`
          - Editing article items in a :ref:`nested article
            <knowledge/articles_editing/create-article>`.
          - Depending on the **parent article**.
        * - :guilabel:`Maintenance`
          - Adding :ref:`equipment <maintenance/equipment_management/add_new_equipment>`.
          - Depending on the **equipment category**.
        * - :guilabel:`Meeting Rooms`
          - Adding a room record.
          - Depending on the **office**.
        * - :guilabel:`Planning`
          - Scheduling a :ref:`planning shift <planning/roles>`.
          - Depending on the planning **role**.
        * - :guilabel:`Project` / :guilabel:`Field Service`
          - Managing a :ref:`task <task_creation/task-configuration>`.
          - Depending on the **project**.
        * - :guilabel:`Recruitment`
          - Creating a :ref:`candidate record <recruitment/quick-add-applicant>`.

            Creating a :ref:`job position <recruitment/new_job_position/edit>`.
          - Depending on the **job position**.

            Depending on the **company**.
        * - :guilabel:`Repairs`
          - Managing a :ref:`repair order <repairs/repair_orders/repair>`.
          - Depending on the **company**.
        * - :guilabel:`Sales`
          - Creating a product.
          - Depending on the **product category**.
