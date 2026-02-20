import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_tooltip(full_path):
    """
    Genera el archivo
    """
    folder_path = os.path.join(full_path, "src", "components", "Tooltips")
    file_path = os.path.join(folder_path, "ThemedTooltip.jsx")

    os.makedirs(folder_path, exist_ok=True)

    content = r"""import { useEffect, useRef, useState } from "react";
import { createPortal } from "react-dom";

export const ThemedTooltip = ({ children, text }) => {
  const [show, setShow] = useState(false);
  const [coords, setCoords] = useState({ top: 0, left: 0 });
  const ref = useRef(null);

  useEffect(() => {
    if (show && ref.current) {
      const rect = ref.current.getBoundingClientRect();
      const tooltipHeight = 30; // altura aprox del tooltip
      const spaceAbove = rect.top;
      const top = spaceAbove < tooltipHeight
        ? rect.bottom + window.scrollY + 8
        : rect.top + window.scrollY - tooltipHeight - 8;

      setCoords({
        top,
        left: rect.left + rect.width / 2,
      });
    }
  }, [show]);

  return (
    <div
      ref={ref}
      className="relative inline-flex"
      onMouseEnter={() => setShow(true)}
      onMouseLeave={() => setShow(false)}
    >
      {children}
      {show &&
        createPortal(
          <div
            style={{
              position: "absolute",
              top: `${coords.top}px`,
              left: `${coords.left}px`,
              transform: "translateX(-50%)",
              zIndex: 9999,
            }}
            className="bg-black text-white text-xs rounded px-2 py-1 shadow-lg whitespace-nowrap"
          >
            {text}
          </div>,
          document.body
        )}
    </div>
  );
};
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)