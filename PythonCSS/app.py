class CSSClasses:
    # Write your CSS classes here!

    # Example classes
    class BgDark:
        """
        This class creates this CSS:
        .bg-dark {
            background-color: #333;
            color: white;
        }

        Use the CSS properties and values
        just like normal, except assign the values
        with the "=" sign.
        """
        background_color = "#333"
        color = "white"

    class DFlex:
        """
        This class makes this CSS:
        .d-flex {
            display: flex;
        }
        """
        display = "flex"

    # You can also inherit from other CSS classes
    class DarkFlexContent(BgDark, DFlex):
        """
        This class will contain the same properties as BgDark
        and Dflex + align-items: center and justify-content: center.
        """
        align_items = "center"
        justify_content = "center"
