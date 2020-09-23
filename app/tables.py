from flask import url_for
from flask_table import Table, Col, LinkCol
from flask_table.html import element


class BaseTable(Table):
    classes = ["table"]
    thead_classes = ["thead-light"]
    allow_empty = True

    def __html__(self):
        tbody = self.tbody()
        if tbody or self.allow_empty:
            content = '\n{thead}\n{tbody}\n{tfoot}\n'.format(
                thead=self.thead(),
                tbody=tbody,
                tfoot=self.tfoot(),
            )
            return element(
                'table',
                attrs=self.get_html_attrs(),
                content=content,
                escape_content=False
            )
        else:
            return element('p', content=self.no_items)

    def tfoot(self):
        tr_content = (
            ''.join(self.tfoot_td(i, col_key, col)
            for i, (col_key, col) in enumerate(self._cols.items())
            if col.show)
        )
        content = element('tr', content=tr_content, escape_content=False)
        return element('tfoot', content=content, escape_content=False)

    def tfoot_td(self, i, key, col):
        if key == "id":
            return element("td", content="#")

        if i == 1:
            url = url_for(".create_model")
            tag = f"<a href='{url}'>Add new</a>"
            return element("td", content=tag, escape_content=False)

        return element("td", content="")


class TestTable(BaseTable):
    id = Col("ID")
    name = Col("Name")
    something = Col("Something")
    created = Col("Created")
    edit = LinkCol("Edit", f".edit_model", url_kwargs={"id": "id"})
