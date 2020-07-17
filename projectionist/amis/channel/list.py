PAGE = {
    "$schema": "http://amis.baidu.com/v1/schemas/page.json#",
    "title": "Book Library",
    "subTitle": "图书 list",
    "toolbar": [
        {
            "type": "button",
            "actionType": "url",
            "label": "新增",
            "icon": "fa fa-plus pull-left",
            "link": "/admin/book/new",
            "blank": True,
            "primary": True,
        },
    ],
    "body": {
        "type": "crud",
        "name":"book list",
        "draggable": False,
        "api": "/api/book/list",
        "keepItemSelectionOnPageChange": True,
        "autoJumpToTopOnPagerChange":True,
        "labelTpl": "${_id} ${id}",
        "perPageAvailable": [5, 10, 25, 50, 100],
        "perPageField": "per_page",
        "primaryField": "_id",
        "filterDefaultVisible": False,
        "bulkActions": [
            {
                "label": "批量删除",
                "actionType": "ajax",
                "api": "delete:/api/book/${ids|raw}",
                "confirmText": "确定要批量删除?"
            },
        ],
        "filterTogglable": False,
        "headerToolbar": [
            "filter-toggler",
            "bulkActions",
            {
                "type": "tpl",
                "tpl": "当前有 ${count} 条数据。",
                "className": "v-middle"
            },
            {
                "type": "columns-toggler",
                "align": "right"
            },
            {
                "type": "drag-toggler",
                "align": "right"
            },
            {
                "type": "pagination",
                "align": "right"
            }
        ],
        "footerToolbar": [
            "statistics",
            "switch-per-page",
            "pagination"
        ],
        "columns": [
            {
                "name": "_id",
                "label": "UUID",
                "sortable": True,
                "searchable": True,
                "type": "text",
                "toggled": True,
                "remark": "UUID",
            },
            {
                "name": "name",
                "label": "书名",
                "sortable": True,
                "searchable": True,
                "type": "text",
                "toggled": True,
            },
            {
                "name": "author_name",
                "label": "作者",
                "sortable": False,
                "type": "text",
                "toggled": True,
                "searchable": True,
            },
            {
                "name": "type",
                "label": "类别",
                "sortable": False,
                "type": "text",
                "toggled": True,
                "searchable": True,
            },
            {
                "name": "belong",
                "label": "归属",
                "sortable": False,
                "type": "text",
                "toggled": True,
                "searchable": True,
            },
            {
                "type": "link",
                "name": "prew_url",
                "label": "文件链接",
                "toggled": True,
                "blank": True
            },
            {
                "name": "cover",
                "label": "Thumbnail",
                "popOver": {
                    "title": "查看大图",
                    "body": "<div class=\"w-xxl\"><img class=\"w-full\" src=\"${cover}\"/></div>",
                },
                "sortable": False,
                "type": "image",
                "toggled": True,
            },
            {
                "name": "updated_text",
                "label": "Updated",
                "sortable": True,
                "type": "text",
                "toggled": True,
            },
            {
                "name": "created_at",
                "label": "Created",
                "sortable": True,
                "type": "datetime",
                "toggled": True,
            },
            {
                "name": "visible",
                "label": "显示",
                "sortable": False,
                "type": "switch",
                "toggled": False,
                "trueValue": True,
                "remark":"该小说展示隐藏",
            },
            {
                "type": "operation",
                "label": "操作",
                "width": 100,
                "buttons": [
                    {
                        "type": "button",
                        "icon": "fa fa-file",
                        "actionType": "url",
                        "tooltip": "详情",
                        "link": "/admin/book/$_id/item",
                        "blank": True
                    },
                    {
                        "type": "button",
                        "icon": "fa fa-bomb text-danger",
                        "actionType": "url",
                        "tooltip": "查看bug",
                        "link": "/admin/book/$_id/buglist",
                        "blank": True
                    },
                    {
                        "type": "button",
                        "icon": "fa fa-eye",
                        "actionType": "dialog",
                        "tooltip": "查看",
                        "dialog": {
                            "title": "查看",
                            "body": {
                                "type": "form",
                                "controls": [
                                    {
                                        "type": "static",
                                        "name": "_id",
                                        "label": "UUID"
                                    },
                                    {
                                        "type": "divider"
                                    },
                                    {
                                        "type": "static",
                                        "name": "id",
                                        "label": "Youtube ID"
                                    },
                                    {
                                        "type": "divider"
                                    },
                                    {
                                        "type": "static",
                                        "name": "title",
                                        "label": "Title"
                                    },
                                    {
                                        "type": "divider"
                                    },
                                    {
                                        "type": "static",
                                        "name": "description",
                                        "label": "Description"
                                    },
                                    {
                                        "type": "divider"
                                    },
                                    {
                                        "type": "static",
                                        "name": "uploader",
                                        "label": "Uploader"
                                    },
                                    {
                                        "type": "divider"
                                    },
                                    {
                                        "type": "image",
                                        "name": "thumbnail",
                                        "label": "Thumbnail"
                                    },
                                ]
                            }
                        }
                    },
                    {
                        "type": "button",
                        "icon": "fa fa-pencil",
                        "tooltip": "编辑",
                        "actionType": "drawer",
                        "drawer": {
                            "position": "left",
                            "size": "lg",
                            "title": "编辑",
                            "body": {
                                "type": "form",
                                "name": "youtube-edit-form",
                                "api": "/api/book/$_id/eidt",
                                "controls": [
                                    {
                                        "type": "text",
                                        "name": "name",
                                        "label": "Title",
                                        "required": True
                                    },
                                    {
                                        "type": "text",
                                        "name": "author_name",
                                        "label": "作者",
                                        "required": True
                                    },
                                    {
                                        "type": "divider"
                                    },
                                    {
                                        "type": "image",
                                        "name": "cover",
                                        "label": "封面"
                                    },
                                ]
                            }
                        }
                    },
                    {
                        "type": "button",
                        "icon": "fa fa-times text-danger",
                        "actionType": "ajax",
                        "tooltip": "删除",
                        "confirmText": "您确认要删除?",
                        "api": "delete:/api/book/$_id"
                    },
                    {
                        "type": "button",
                        "icon": "fa fa-ban text-danger",
                        "actionType": "ajax",
                        "tooltip": "显示",
                        "api":"get:/api/book/$_id/visible",
                    },
                ],
                "toggled": True
            }
        ]
    }
}