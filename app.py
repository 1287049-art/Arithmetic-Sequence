import streamlit as st
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for Streamlit
import matplotlib.pyplot as plt
import numpy as np

def generate_arithmetic_sequence(first_term, common_difference, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_difference (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: A list containing the arithmetic sequence
    """
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_difference)
        sequence.append(term)
    return sequence

def generate_geometric_sequence(first_term, common_ratio, num_terms):
    """
    Generate a geometric sequence given the first term, common ratio, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_ratio (float): The common ratio between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: A list containing the geometric sequence
    """
    sequence = []
    for i in range(num_terms):
        term = first_term * (common_ratio ** i)
        sequence.append(term)
    return sequence

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title
    st.title("🔢 Sequence Generator")
    st.write("Generate arithmetic or geometric sequences with detailed formulas and visualizations.")
    
    # Sequence type selector
    sequence_type = st.radio(
        "Choose Sequence Type:",
        ["Arithmetic Sequence", "Geometric Sequence"],
        index=0,
        help="Select whether to generate an arithmetic or geometric sequence"
    )
    
    # Create input section
    st.header("Input Parameters")
    
    # Create three columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0 if sequence_type == "Geometric Sequence" else 0.0,
            step=1.0,
            help=f"The first term of the {sequence_type.lower()}"
        )
    
    with col2:
        if sequence_type == "Arithmetic Sequence":
            second_param = st.number_input(
                "Common Difference (d)",
                value=1.0,
                step=1.0,
                help="The constant difference between consecutive terms"
            )
        else:
            second_param = st.number_input(
                "Common Ratio (r)",
                value=2.0,
                step=0.1,
                help="The constant ratio between consecutive terms"
            )
    
    with col3:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (maximum 1000)"
        )
    
    # Input validation and sequence generation
    if num_terms > 0:
        try:
            # Generate the sequence based on type
            if sequence_type == "Arithmetic Sequence":
                sequence = generate_arithmetic_sequence(first_term, second_param, num_terms)
            else:
                sequence = generate_geometric_sequence(first_term, second_param, num_terms)
            
            # Normalize variables for both sequence types
            is_arith = sequence_type.startswith("Arithmetic")
            param_value = second_param
            param_symbol = "d" if is_arith else "r"
            param_label = "Common Difference" if is_arith else "Common Ratio"
            file_prefix = "arithmetic" if is_arith else "geometric"
            param_key = "common_difference" if is_arith else "common_ratio"
            
            # Enhanced Formula Display
            if is_arith:
                st.header("📐 Arithmetic Sequence Formulas")
                
                # General formula
                st.subheader("General Formula for nth Term:")
                st.latex(r"a_n = a_1 + (n-1) \times d")
                
                # Specific formula with values
                st.subheader("Your Sequence Formula:")
                if param_value >= 0:
                    st.latex(f"a_n = {first_term} + (n-1) \\times {param_value}")
                else:
                    st.latex(f"a_n = {first_term} + (n-1) \\times ({param_value})")
                
                # Show first few terms with formula
                st.subheader("First Few Terms:")
                formula_examples = []
                for i in range(1, min(6, int(num_terms) + 1)):
                    term_value = first_term + (i-1) * param_value
                    if param_value >= 0:
                        formula_examples.append(f"a_{{{i}}} = {first_term} + ({i}-1) × {param_value} = {term_value}")
                    else:
                        formula_examples.append(f"a_{{{i}}} = {first_term} + ({i}-1) × ({param_value}) = {term_value}")
                
                for example in formula_examples:
                    st.write(f"• {example}")
            else:
                st.header("📐 Geometric Sequence Formulas")
                
                # General formula
                st.subheader("General Formula for nth Term:")
                st.latex(r"a_n = a_1 \times r^{(n-1)}")
                
                # Specific formula with values
                st.subheader("Your Sequence Formula:")
                if param_value >= 0:
                    st.latex(f"a_n = {first_term} \\times {param_value}^{{{{(n-1)}}}}")
                else:
                    st.latex(f"a_n = {first_term} \\times ({param_value})^{{{{(n-1)}}}}")
                
                # Show first few terms with formula
                st.subheader("First Few Terms:")
                formula_examples = []
                for i in range(1, min(6, int(num_terms) + 1)):
                    term_value = first_term * (param_value ** (i-1))
                    if param_value >= 0:
                        formula_examples.append(f"a_{{{i}}} = {first_term} × {param_value}^{{{i-1}}} = {term_value}")
                    else:
                        formula_examples.append(f"a_{{{i}}} = {first_term} × ({param_value})^{{{i-1}}} = {term_value}")
                
                for example in formula_examples:
                    st.write(f"• {example}")
            
            # Display sequence information
            st.header("Sequence Information")
            info_col1, info_col2, info_col3 = st.columns(3)
            
            with info_col1:
                st.metric("First Term", f"{first_term}")
            
            with info_col2:
                st.metric(param_label, f"{param_value}")
            
            with info_col3:
                st.metric("Number of Terms", f"{int(num_terms)}")
            
            # Display the sequence
            st.header("Generated Sequence")
            
            # Show sequence as a formatted list
            if len(sequence) <= 50:  # Show all terms if 50 or fewer
                sequence_str = ", ".join([str(term) for term in sequence])
                st.write(f"**Sequence:** {sequence_str}")
            else:  # Show first 25 and last 25 terms if more than 50
                first_part = sequence[:25]
                last_part = sequence[-25:]
                first_str = ", ".join([str(term) for term in first_part])
                last_str = ", ".join([str(term) for term in last_part])
                st.write(f"**First 25 terms:** {first_str}")
                st.write("...")
                st.write(f"**Last 25 terms:** {last_str}")
            
            # Add matplotlib visualization
            st.header("📊 Sequence Visualization")
            
            # Create the plot
            fig, ax = plt.subplots(figsize=(12, 6))
            
            # Determine how many points to plot
            plot_points = min(len(sequence), 100)  # Limit to 100 points for readability
            x_values = list(range(1, plot_points + 1))
            y_values = sequence[:plot_points]
            
            # Create scatter plot and line plot
            ax.scatter(x_values, y_values, color='blue', s=50, alpha=0.7, zorder=3)
            ax.plot(x_values, y_values, color='red', linewidth=2, alpha=0.8, zorder=2)
            
            # Customize the plot
            ax.set_xlabel('Term Number (n)', fontsize=12)
            ax.set_ylabel('Term Value (aₙ)', fontsize=12)
            ax.set_title(f'{sequence_type}: a₁={first_term}, {param_symbol}={param_value}', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            
            # Add some styling
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            # Show every nth x-tick to avoid crowding
            if plot_points > 20:
                tick_step = max(1, plot_points // 10)
                ax.set_xticks(range(1, plot_points + 1, tick_step))
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
            
            if len(sequence) > 100:
                st.info(f"📝 Note: Chart shows first 100 terms. Your sequence has {len(sequence)} terms total.")
            
            # Download section
            st.header("Download Options")
            download_col1, download_col2, download_col3 = st.columns(3)
            
            # Create a table showing term number and value
            import pandas as pd
            import json
            
            df = pd.DataFrame({
                'Term Number (n)': range(1, len(sequence) + 1),
                'Term Value (aₙ)': sequence
            })
            
            # Download as CSV
            with download_col1:
                csv_data = df.to_csv(index=False)
                st.download_button(
                    label="📄 Download CSV",
                    data=csv_data,
                    file_name=f"{file_prefix}_sequence_{first_term}_{param_value}_{int(num_terms)}.csv",
                    mime="text/csv",
                    help="Download sequence as CSV file"
                )
            
            # Download as Text
            with download_col2:
                text_data = f"{sequence_type}\n"
                text_data += f"First Term: {first_term}\n"
                text_data += f"{param_label}: {param_value}\n"
                text_data += f"Number of Terms: {int(num_terms)}\n"
                text_data += f"Sum: {sum(sequence)}\n\n"
                text_data += "Sequence: " + ", ".join([str(term) for term in sequence])
                
                st.download_button(
                    label="📝 Download Text",
                    data=text_data,
                    file_name=f"{file_prefix}_sequence_{first_term}_{param_value}_{int(num_terms)}.txt",
                    mime="text/plain",
                    help="Download sequence as text file"
                )
            
            # Download as JSON
            with download_col3:
                json_data = {
                    "sequence_type": sequence_type,
                    "parameters": {
                        "first_term": first_term,
                        param_key: param_value,
                        "number_of_terms": int(num_terms)
                    },
                    "sequence": sequence,
                    "sum": sum(sequence),
                    "last_term": sequence[-1]
                }
                
                st.download_button(
                    label="📊 Download JSON",
                    data=json.dumps(json_data, indent=2),
                    file_name=f"{file_prefix}_sequence_{first_term}_{param_value}_{int(num_terms)}.json",
                    mime="application/json",
                    help="Download sequence as JSON file"
                )
            
            # Display in expandable table format
            with st.expander("View Detailed Table", expanded=False):
                st.dataframe(df, width=650)
            
            # Enhanced Sum Information
            st.header(f"🧮 Sum of {sequence_type} (Sₙ)")
            
            last_term = sequence[-1]
            sequence_sum = sum(sequence)
            
            # Display sum metrics
            sum_col1, sum_col2, sum_col3 = st.columns(3)
            with sum_col1:
                st.metric("Sum (Sₙ)", f"{sequence_sum}")
                st.caption("Sum of all terms")
            with sum_col2:
                st.metric("Last Term (aₙ)", f"{last_term}")
                st.caption(f"The {int(num_terms)}th term")
            with sum_col3:
                st.metric("Average Term", f"{sequence_sum/num_terms:.2f}")
                st.caption("Mean of all terms")
            
            # Show sum formulas based on sequence type
            st.subheader("Sum Formulas:")
            
            if is_arith:
                # Arithmetic sequence sum formulas
                st.write("**General Formulas:**")
                st.latex(r"S_n = \frac{n(a_1 + a_n)}{2} \quad \text{or} \quad S_n = \frac{n(2a_1 + (n-1)d)}{2}")
                
                # Specific calculation with your values
                st.write("**Your Sequence Calculation:**")
                st.latex(f"S_{{{int(num_terms)}}} = \\frac{{{int(num_terms)}(a_1 + a_{{{int(num_terms)}}})}}{{2}} = \\frac{{{int(num_terms)}({first_term} + {last_term})}}{{2}} = {sequence_sum}")
                
                # Alternative formula calculation
                st.write("**Alternative Calculation:**")
                alternative_calc = f"{int(num_terms)}(2 \\times {first_term} + ({int(num_terms)}-1) \\times {param_value})"
                if param_value < 0:
                    alternative_calc = f"{int(num_terms)}(2 \\times {first_term} + ({int(num_terms)}-1) \\times ({param_value}))"
                st.latex(f"S_{{{int(num_terms)}}} = \\frac{{{alternative_calc}}}{{2}} = {sequence_sum}")
            else:
                # Geometric sequence sum formulas
                st.write("**General Formula:**")
                if param_value == 1:
                    st.latex(r"S_n = n \times a_1 \quad \text{(when r = 1)}")
                    st.write("**Your Sequence Calculation:**")
                    st.latex(f"S_{{{int(num_terms)}}} = {int(num_terms)} \\times {first_term} = {sequence_sum}")
                else:
                    st.latex(r"S_n = a_1 \times \frac{1 - r^n}{1 - r} \quad \text{(when r ≠ 1)}")
                    st.write("**Your Sequence Calculation:**")
                    if param_value >= 0:
                        st.latex(f"S_{{{int(num_terms)}}} = {first_term} \\times \\frac{{{{1 - {param_value}^{{{int(num_terms)}}}}}}}{{{{1 - {param_value}}}}} = {sequence_sum}")
                    else:
                        st.latex(f"S_{{{int(num_terms)}}} = {first_term} \\times \\frac{{{{1 - ({param_value})^{{{int(num_terms)}}}}}}}{{{{1 - ({param_value})}}}} = {sequence_sum}")
            
            # Additional Information
            st.header("📋 Additional Information")
            info_col1, info_col2 = st.columns(2)
            
            with info_col1:
                st.write("**Sequence Properties:**")
                st.write(f"• First term (a₁): {first_term}")
                st.write(f"• {param_label} ({param_symbol}): {param_value}")
                st.write(f"• Number of terms (n): {int(num_terms)}")
                
                if is_arith:
                    if param_value > 0:
                        st.write("• Type: Increasing sequence")
                    elif param_value < 0:
                        st.write("• Type: Decreasing sequence")
                    else:
                        st.write("• Type: Constant sequence")
                else:
                    if param_value > 1:
                        st.write("• Type: Increasing geometric sequence")
                    elif param_value == 1:
                        st.write("• Type: Constant sequence")
                    elif 0 < param_value < 1:
                        st.write("• Type: Decreasing geometric sequence")
                    elif param_value == 0:
                        st.write("• Type: Zero sequence (after first term)")
                    else:
                        st.write("• Type: Alternating geometric sequence")
            
            with info_col2:
                st.write("**Calculated Values:**")
                st.write(f"• Last term (a_{{{int(num_terms)}}}): {last_term}")
                st.write(f"• Sum of sequence (S_{{{int(num_terms)}}}): {sequence_sum}")
                st.write(f"• Average term: {sequence_sum/num_terms:.2f}")
                st.write(f"• Range: {last_term - first_term}")
            
        except Exception as e:
            st.error(f"An error occurred while generating the sequence: {str(e)}")
    else:
        st.warning("Please enter a positive number of terms.")
    
    # Add footer with information
    st.markdown("---")
    st.markdown(
        """
        ### About Arithmetic Sequences
        
        An arithmetic sequence is a sequence of numbers where each term after the first is obtained by adding a constant value (common difference) to the previous term.
        
        - **Formula for nth term:** aₙ = a₁ + (n-1)d
        - **Formula for sum:** Sₙ = n(a₁ + aₙ)/2 or Sₙ = n(2a₁ + (n-1)d)/2
        
        Where:
        - a₁ = first term
        - d = common difference  
        - n = number of terms
        - aₙ = nth term
        - Sₙ = sum of first n terms
        """
    )

if __name__ == "__main__":
    main()
