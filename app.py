import streamlit as st

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

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    # Main title
    st.title("🔢 Arithmetic Sequence Generator")
    st.write("Generate arithmetic sequences by specifying the first term, common difference, and number of terms.")
    
    # Create input section
    st.header("Input Parameters")
    
    # Create three columns for better layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=0.0,
            step=1.0,
            help="The first term of the arithmetic sequence"
        )
    
    with col2:
        common_difference = st.number_input(
            "Common Difference (d)",
            value=1.0,
            step=1.0,
            help="The constant difference between consecutive terms"
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
            # Generate the arithmetic sequence
            sequence = generate_arithmetic_sequence(first_term, common_difference, num_terms)
            
            # Display the formula
            st.header("Formula")
            st.latex(f"a_n = {first_term} + (n-1) \\times {common_difference}")
            
            # Display sequence information
            st.header("Sequence Information")
            info_col1, info_col2, info_col3 = st.columns(3)
            
            with info_col1:
                st.metric("First Term", f"{first_term}")
            
            with info_col2:
                st.metric("Common Difference", f"{common_difference}")
            
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
            
            # Display in expandable table format
            with st.expander("View Detailed Table", expanded=False):
                # Create a table showing term number and value
                import pandas as pd
                
                df = pd.DataFrame({
                    'Term Number (n)': range(1, len(sequence) + 1),
                    'Term Value (aₙ)': sequence
                })
                
                st.dataframe(df, use_container_width=True)
            
            # Additional calculations
            st.header("Additional Information")
            calc_col1, calc_col2 = st.columns(2)
            
            with calc_col1:
                st.metric("Sum of Sequence", f"{sum(sequence)}")
                st.caption("Sum of all terms in the sequence")
            
            with calc_col2:
                last_term = sequence[-1]
                st.metric("Last Term", f"{last_term}")
                st.caption(f"The {int(num_terms)}th term of the sequence")
            
            # Show the sum formula
            st.subheader("Sum Formula")
            st.latex(f"S_n = \\frac{{n(a_1 + a_n)}}{2} = \\frac{{{int(num_terms)}({first_term} + {last_term})}}{2} = {sum(sequence)}")
            
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
